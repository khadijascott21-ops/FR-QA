package com.komatsu.currencyconverter;

import com.googlecode.lanterna.gui2.MultiWindowTextGUI;
import com.googlecode.lanterna.screen.Screen;
import com.googlecode.lanterna.screen.TerminalScreen;
import com.googlecode.lanterna.terminal.DefaultTerminalFactory;
import com.komatsu.currencyconverter.service.CurrencyConverter;
import com.komatsu.currencyconverter.ui.ConverterWindow;
import java.io.IOException;

/**
 * Application entry point; starts the Lanterna text GUI.
 */
public final class App {

    private App() {
    }

    /**
     * Launches the converter and blocks until the user quits.
     *
     * @param args ignored
     * @throws IOException if the terminal cannot be used
     */
    public static void main(String[] args) throws IOException {
        try (Screen screen = new TerminalScreen(new DefaultTerminalFactory().createTerminal())) {
            screen.startScreen();
            new MultiWindowTextGUI(screen).addWindowAndWait(new ConverterWindow(new CurrencyConverter()));
        }
    }
}
