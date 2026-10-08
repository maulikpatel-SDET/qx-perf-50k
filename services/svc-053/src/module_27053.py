"""Service module 27053: business logic, no crypto."""


def calculate_total_27053(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27053():
    return 'module 27053 handles orders and invoices'
