"""Service module 29071: business logic, no crypto."""


def calculate_total_29071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29071():
    return 'module 29071 handles orders and invoices'
