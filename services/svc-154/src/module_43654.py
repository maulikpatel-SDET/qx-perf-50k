"""Service module 43654: business logic, no crypto."""


def calculate_total_43654(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43654():
    return 'module 43654 handles orders and invoices'
