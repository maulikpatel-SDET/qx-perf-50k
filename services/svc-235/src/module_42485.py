"""Service module 42485: business logic, no crypto."""


def calculate_total_42485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42485():
    return 'module 42485 handles orders and invoices'
