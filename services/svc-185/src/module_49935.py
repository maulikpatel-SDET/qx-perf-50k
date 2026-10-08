"""Service module 49935: business logic, no crypto."""


def calculate_total_49935(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49935():
    return 'module 49935 handles orders and invoices'
