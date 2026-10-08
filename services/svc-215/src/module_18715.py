"""Service module 18715: business logic, no crypto."""


def calculate_total_18715(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18715():
    return 'module 18715 handles orders and invoices'
