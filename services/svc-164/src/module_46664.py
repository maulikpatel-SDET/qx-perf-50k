"""Service module 46664: business logic, no crypto."""


def calculate_total_46664(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46664():
    return 'module 46664 handles orders and invoices'
