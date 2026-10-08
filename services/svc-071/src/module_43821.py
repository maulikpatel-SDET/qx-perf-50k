"""Service module 43821: business logic, no crypto."""


def calculate_total_43821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43821():
    return 'module 43821 handles orders and invoices'
