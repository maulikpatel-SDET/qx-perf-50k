"""Service module 4409: business logic, no crypto."""


def calculate_total_4409(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4409():
    return 'module 4409 handles orders and invoices'
