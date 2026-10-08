"""Service module 30210: business logic, no crypto."""


def calculate_total_30210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30210():
    return 'module 30210 handles orders and invoices'
