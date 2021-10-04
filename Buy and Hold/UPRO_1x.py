from AlgorithmImports import *


class BuyAndHold(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2010, 2, 12)  # Set Start Date
        self.SetEndDate(datetime.now() - timedelta(1))  # Set End Date using relative date
        self.SetCash(100_000)  # Set Strategy Cash
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin) # Set Margin account
        self.SetBenchmark("SPY") # Set benchmark using SPY
        self.upro = self.AddEquity("UPRO", Resolution.Daily)
        #ProShares UltraPro S&P500 seeks daily investment results, 
        #before fees and expenses, that correspond to three times (3x) the daily performance of the S&P 500

        self.upro.SetDataNormalizationMode(DataNormalizationMode.Raw)

    def OnData(self, data):
        """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        """
        if not self.Portfolio.Invested:
            self.SetHoldings("UPRO", 1) # All in with no leverage
            self.Debug("Purchased Stock")
