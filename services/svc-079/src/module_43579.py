"""Service module 43579: business logic, no crypto."""


def calculate_total_43579(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43579():
    return 'module 43579 handles orders and invoices'
