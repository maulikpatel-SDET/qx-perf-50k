"""Service module 15579: business logic, no crypto."""


def calculate_total_15579(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15579():
    return 'module 15579 handles orders and invoices'
