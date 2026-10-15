package com.komatsu.currencyconverter.unit;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertFalse;
import static org.testng.Assert.assertTrue;

import com.komatsu.currencyconverter.service.CurrencyConverter;
import com.komatsu.currencyconverter.ui.ConversionView;
import com.komatsu.currencyconverter.ui.ConverterPresenter;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

/** Unit tests for {@link ConverterPresenter} using a recording view. */
public class ConverterPresenterTest {

    private static final class RecordingView implements ConversionView {
        boolean visible;
        String amount = "";
        String rate = "";
        String error = "";

        @Override
        public void showResult(String convertedAmount, String exchangeRate) {
            visible = true;
            amount = convertedAmount;
            rate = exchangeRate;
        }

        @Override
        public void hideResult() {
            visible = false;
        }

        @Override
        public void showError(String message) {
            error = message;
        }
    }

    private RecordingView view;
    private ConverterPresenter presenter;

    @BeforeMethod
    public void setUp() {
        view = new RecordingView();
        presenter = new ConverterPresenter(new CurrencyConverter(), view);
        presenter.onSourceChanged("USD");
        presenter.onTargetChanged("EUR");
    }

    @Test
    public void showsFormattedResult() {
        presenter.onAmountChanged("100");
        assertTrue(view.visible);
        assertEquals(view.amount, "86.26");
        assertEquals(view.rate, "0.862623");
    }

    @Test
    public void updatesWhenCurrencyChanges() {
        presenter.onAmountChanged("100");
        presenter.onTargetChanged("JPY");
        assertEquals(view.amount, "15925.07");
    }

    @Test
    public void emptyAmountHidesResult() {
        presenter.onAmountChanged("100");
        presenter.onAmountChanged("");
        assertFalse(view.visible);
    }

    @Test
    public void nonNumericAmountShowsError() {
        presenter.onAmountChanged("abc");
        assertFalse(view.visible);
        assertEquals(view.error, "Amount must be a number");
    }

    @Test
    public void nonPositiveAmountShowsError() {
        presenter.onAmountChanged("-3");
        assertFalse(view.visible);
        assertFalse(view.error.isEmpty());
    }
}
