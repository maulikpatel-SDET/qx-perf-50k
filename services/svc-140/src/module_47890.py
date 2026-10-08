"""Service module 47890: business logic, no crypto."""


def calculate_total_47890(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47890():
    return 'module 47890 handles orders and invoices'
