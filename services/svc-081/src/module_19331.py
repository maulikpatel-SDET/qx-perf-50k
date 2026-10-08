"""Service module 19331: business logic, no crypto."""


def calculate_total_19331(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19331():
    return 'module 19331 handles orders and invoices'
