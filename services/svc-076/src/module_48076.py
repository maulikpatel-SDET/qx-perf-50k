"""Service module 48076: business logic, no crypto."""


def calculate_total_48076(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48076():
    return 'module 48076 handles orders and invoices'
