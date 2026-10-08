"""Service module 27219: business logic, no crypto."""


def calculate_total_27219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27219():
    return 'module 27219 handles orders and invoices'
