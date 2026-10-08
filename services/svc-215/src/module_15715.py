"""Service module 15715: business logic, no crypto."""


def calculate_total_15715(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15715():
    return 'module 15715 handles orders and invoices'
