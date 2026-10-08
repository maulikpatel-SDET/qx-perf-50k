"""Service module 43959: business logic, no crypto."""


def calculate_total_43959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43959():
    return 'module 43959 handles orders and invoices'
