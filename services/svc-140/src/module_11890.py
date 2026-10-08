"""Service module 11890: business logic, no crypto."""


def calculate_total_11890(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11890():
    return 'module 11890 handles orders and invoices'
