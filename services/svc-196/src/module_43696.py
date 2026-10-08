"""Service module 43696: business logic, no crypto."""


def calculate_total_43696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43696():
    return 'module 43696 handles orders and invoices'
