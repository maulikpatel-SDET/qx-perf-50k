"""Service module 43997: business logic, no crypto."""


def calculate_total_43997(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43997():
    return 'module 43997 handles orders and invoices'
