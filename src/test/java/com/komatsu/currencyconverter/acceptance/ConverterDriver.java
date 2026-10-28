package com.komatsu.currencyconverter.acceptance;

import com.googlecode.lanterna.TerminalSize;
import com.googlecode.lanterna.gui2.MultiWindowTextGUI;
import com.googlecode.lanterna.screen.TerminalScreen;
import com.googlecode.lanterna.terminal.virtual.DefaultVirtualTerminal;
import com.komatsu.currencyconverter.service.CurrencyConverter;
import com.komatsu.currencyconverter.ui.ConverterWindow;
import java.io.IOException;
import java.io.UncheckedIOException;
import java.time.Duration;
import java.util.function.BooleanSupplier;

/**
 * Test driver operating the real Lanterna GUI on a headless virtual terminal.
 */
public class ConverterDriver implements AutoCloseable {

    private static final Duration DEFAULT_TIMEOUT = Duration.ofSeconds(5);

    private final TerminalScreen screen;
    private final MultiWindowTextGUI gui;
    private final ConverterWindow window = new ConverterWindow(new CurrencyConverter());

    /** Starts the application window on a virtual terminal. */
    public ConverterDriver() {
        try {
            screen = new TerminalScreen(new DefaultVirtualTerminal(new TerminalSize(100, 30)));
            screen.startScreen();
            gui = new MultiWindowTextGUI(screen);
            gui.addWindow(window);
            render();
        } catch (IOException e) {
            throw new UncheckedIOException(e);
        }
    }

    /**
     * Types an amount into the amount field.
     *
     * @param text amount text
     */
    public void enterAmount(String text) {
        window.setAmount(text);
        render();
    }

    /**
     * Selects the source currency in its dropdown.
     *
     * @param code currency code
     */
    public void selectSource(String code) {
        window.selectSource(code);
        render();
    }

    /**
     * Selects the target currency in its dropdown.
     *
     * @param code currency code
     */
    public void selectTarget(String code) {
        window.selectTarget(code);
        render();
    }

    /**
     * Waits until the result container is visible.
     *
     * @return true if it became visible before the timeout
     */
    public boolean waitForResult() {
        return waitUntil(window::isResultVisible, DEFAULT_TIMEOUT);
    }

    /**
     * Returns the window under test.
     *
     * @return the window
     */
    public ConverterWindow window() {
        return window;
    }

    private boolean waitUntil(BooleanSupplier condition, Duration timeout) {
        long deadline = System.nanoTime() + timeout.toNanos();
        while (System.nanoTime() < deadline) {
            render();
            if (condition.getAsBoolean()) {
                return true;
            }
            try {
                Thread.sleep(25);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                return false;
            }
        }
        return condition.getAsBoolean();
    }

    private void render() {
        try {
            // Process queued dropdown listeners before reading or drawing the result.
            gui.getGUIThread().processEventsAndUpdate();
        } catch (IOException e) {
            throw new UncheckedIOException(e);
        }
    }

    @Override
    public void close() {
        try {
            window.close();
            screen.stopScreen();
        } catch (IOException e) {
            throw new UncheckedIOException(e);
        }
    }
}
