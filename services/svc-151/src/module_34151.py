"""Service module 34151: business logic, no crypto."""


def calculate_total_34151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34151():
    return 'module 34151 handles orders and invoices'
