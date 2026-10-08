"""Service module 49817: business logic, no crypto."""


def calculate_total_49817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49817():
    return 'module 49817 handles orders and invoices'
