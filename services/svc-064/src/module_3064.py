"""Service module 3064: business logic, no crypto."""


def calculate_total_3064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3064():
    return 'module 3064 handles orders and invoices'
