"""Service module 9430: business logic, no crypto."""


def calculate_total_9430(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9430():
    return 'module 9430 handles orders and invoices'
