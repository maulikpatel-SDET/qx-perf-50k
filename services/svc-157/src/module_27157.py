"""Service module 27157: business logic, no crypto."""


def calculate_total_27157(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27157():
    return 'module 27157 handles orders and invoices'
