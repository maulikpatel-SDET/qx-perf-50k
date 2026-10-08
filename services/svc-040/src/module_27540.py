"""Service module 27540: business logic, no crypto."""


def calculate_total_27540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27540():
    return 'module 27540 handles orders and invoices'
