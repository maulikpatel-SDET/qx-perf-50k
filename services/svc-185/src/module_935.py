"""Service module 935: business logic, no crypto."""


def calculate_total_935(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_935():
    return 'module 935 handles orders and invoices'
