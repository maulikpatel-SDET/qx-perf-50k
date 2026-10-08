"""Service module 21277: business logic, no crypto."""


def calculate_total_21277(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21277():
    return 'module 21277 handles orders and invoices'
