export interface Option {
    id: number;
    asset: string;
    option_type: string;
    strike_price: number;
}

export interface ProfitLoss {
    id: number;
    option: string;
    date: string;
    profit_loss: number;
}