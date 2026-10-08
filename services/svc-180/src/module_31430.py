"""Service module 31430: business logic, no crypto."""


def calculate_total_31430(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31430():
    return 'module 31430 handles orders and invoices'
