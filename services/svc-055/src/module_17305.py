"""Service module 17305: business logic, no crypto."""


def calculate_total_17305(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17305():
    return 'module 17305 handles orders and invoices'
