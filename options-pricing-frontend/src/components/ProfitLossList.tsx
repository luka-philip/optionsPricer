// src/components/ProfitLossList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {ProfitLoss} from "../common/types";

function ProfitLossList() {
    const [profitLoss, setProfitLoss] = useState<ProfitLoss[]>([]);

    useEffect(() => {
        // Make an API request to fetch P&L data
        axios.get('/api/profit-loss/')
            .then((response) => {
                setProfitLoss(response.data);
            })
            .catch((error) => {
                console.error('Error fetching P&L data:', error);
            });
    }, []);

    return (
        <div>
            <h2>P&L Records</h2>
            <ul>
                {profitLoss.map((record) => (
                    <li key={record.id}>
                        Option: {record.option} - Date: {record.date} - P&L: {record.profit_loss}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ProfitLossList;