"""Service module 43688: business logic, no crypto."""


def calculate_total_43688(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43688():
    return 'module 43688 handles orders and invoices'
