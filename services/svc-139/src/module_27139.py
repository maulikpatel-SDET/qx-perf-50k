"""Service module 27139: business logic, no crypto."""


def calculate_total_27139(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27139():
    return 'module 27139 handles orders and invoices'
