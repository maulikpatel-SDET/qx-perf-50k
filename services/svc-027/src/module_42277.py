"""Service module 42277: business logic, no crypto."""


def calculate_total_42277(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42277():
    return 'module 42277 handles orders and invoices'
