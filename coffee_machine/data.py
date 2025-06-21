# repetitive menu key names

INGREDIENTS = "ingredients"
PRICE = "price"

WATER = "water"
MILK = "milk"
COFFEE = "coffee"

UNITS = "units"
CURRENCY_KEY = "currency"
AMOUNT = "amount"

MILLILITERS = "mL"
GRAMS = "g"
CURRENCY = "CAD $"

menu = {
    "espresso": {
        INGREDIENTS: {
            WATER: {
                UNITS: MILLILITERS,
                AMOUNT: 75,
            },
            MILK: {
                UNITS: MILLILITERS,
                AMOUNT: 0,
            },
            COFFEE: {
                UNITS: GRAMS,
                AMOUNT: 16,
            },
        },
        PRICE: {
            CURRENCY_KEY: CURRENCY,
            AMOUNT: 5.5,
        },
    },
    "americano": {
        INGREDIENTS: {
            WATER: {
                UNITS: MILLILITERS,
                AMOUNT: 250,
            },
            MILK: {
                UNITS: MILLILITERS,
                AMOUNT: 0,
            },
            COFFEE: {
                UNITS: GRAMS,
                AMOUNT: 16,
            },
        },
        PRICE: {
            CURRENCY_KEY: "CAD $",
            AMOUNT: 6,
        },
    },
    "capuccino": {
        INGREDIENTS: {
            WATER: {
                UNITS: MILLILITERS,
                AMOUNT: 50,
            },
            MILK: {
                UNITS: MILLILITERS,
                AMOUNT: 200,
            },
            COFFEE: {
                UNITS: GRAMS,
                AMOUNT: 16,
            },
        },
        PRICE: {
            CURRENCY_KEY: "CAD $",
            AMOUNT: 7.25,
        },
    },
    "latte": {
        INGREDIENTS: {
            WATER: {
                UNITS: MILLILITERS,
                AMOUNT: 50,
            },
            MILK: {
                UNITS: MILLILITERS,
                AMOUNT: 250,
            },
            COFFEE: {
                UNITS: GRAMS,
                AMOUNT: 16,
            },
        },
        PRICE: {
            CURRENCY_KEY: "CAD $",
            AMOUNT: 8,
        },
    },
}

supplies = {
    WATER: {
        UNITS: MILLILITERS,
        AMOUNT: 400,
    },
    MILK: {
        UNITS: MILLILITERS,
        AMOUNT: 900,
    },
    COFFEE: {
        UNITS: GRAMS,
        AMOUNT: 200,
    },
}

coins = {
    "toonies": 2,
    "loonies": 1,
    "quarters": 0.25,
    "dimes": 0.1,
    "nickels": 0.05,
}