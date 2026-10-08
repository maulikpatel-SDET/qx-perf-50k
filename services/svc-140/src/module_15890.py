"""Service module 15890: business logic, no crypto."""


def calculate_total_15890(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15890():
    return 'module 15890 handles orders and invoices'
