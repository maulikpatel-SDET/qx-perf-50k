"""Service module 6715: business logic, no crypto."""


def calculate_total_6715(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6715():
    return 'module 6715 handles orders and invoices'
