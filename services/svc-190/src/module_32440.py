"""Service module 32440: business logic, no crypto."""


def calculate_total_32440(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32440():
    return 'module 32440 handles orders and invoices'
