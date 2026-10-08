"""Service module 31966: business logic, no crypto."""


def calculate_total_31966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31966():
    return 'module 31966 handles orders and invoices'
