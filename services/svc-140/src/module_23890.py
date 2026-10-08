"""Service module 23890: business logic, no crypto."""


def calculate_total_23890(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23890():
    return 'module 23890 handles orders and invoices'
