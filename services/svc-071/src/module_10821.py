"""Service module 10821: business logic, no crypto."""


def calculate_total_10821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10821():
    return 'module 10821 handles orders and invoices'
