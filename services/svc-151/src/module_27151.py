"""Service module 27151: business logic, no crypto."""


def calculate_total_27151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27151():
    return 'module 27151 handles orders and invoices'
