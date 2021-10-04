from AlgorithmImports import *


class BuyAndHold(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2010, 2, 12)  # Set Start Date
        self.SetEndDate(datetime.now() - timedelta(1))  # Set End Date using relative date
        self.SetCash(100_000)  # Set Strategy Cash
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin) # Set Margin account
        self.SetBenchmark("SPY") # Set benchmark using SPY
        self.qqq = self.AddEquity("QQQ", Resolution.Daily)
    

        self.qqq.SetDataNormalizationMode(DataNormalizationMode.Raw)

    def OnData(self, data):
        """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        """
        if not self.Portfolio.Invested:
            self.SetHoldings("QQQ", 1) # All in with no leverage
            self.Debug("Purchased Stock")
