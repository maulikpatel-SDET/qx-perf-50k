"""Service module 49631: business logic, no crypto."""


def calculate_total_49631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49631():
    return 'module 49631 handles orders and invoices'
