"""Service module 11071: business logic, no crypto."""


def calculate_total_11071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11071():
    return 'module 11071 handles orders and invoices'
