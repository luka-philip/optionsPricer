// src/components/OptionList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {Option} from "../common/types";

function OptionList() {
    const [options , setOptions] = useState<Option[]>([]);

    useEffect(() => {
        // Make an API request to fetch options data
        axios.get('/api/options/')
            .then((response) => {
                setOptions(response.data);
            })
            .catch((error) => {
                console.error('Error fetching options:', error);
            });
    }, []);

    return (
        <div>
            <h2>Options List</h2>
            <ul>
                {options.map((option) => (
                    <li key={option.id}>
                        {option.asset} - {option.option_type} - Strike: {option.strike_price}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default OptionList;