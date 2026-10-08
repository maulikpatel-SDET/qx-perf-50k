"""Service module 49187: business logic, no crypto."""


def calculate_total_49187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49187():
    return 'module 49187 handles orders and invoices'
