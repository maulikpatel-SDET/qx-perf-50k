"""Service module 27837: business logic, no crypto."""


def calculate_total_27837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27837():
    return 'module 27837 handles orders and invoices'
