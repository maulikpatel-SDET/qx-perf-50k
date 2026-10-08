"""Service module 44036: business logic, no crypto."""


def calculate_total_44036(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44036():
    return 'module 44036 handles orders and invoices'
