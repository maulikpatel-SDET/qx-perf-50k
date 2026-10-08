"""Service module 33821: business logic, no crypto."""


def calculate_total_33821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33821():
    return 'module 33821 handles orders and invoices'
